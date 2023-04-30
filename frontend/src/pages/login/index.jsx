import React, { useState, useEffect, useContext } from 'react'
import { Navigate } from 'react-router-dom';
import { UserContext } from '../../App';
import { Box, useTheme, Typography } from '@mui/material';
import { tokens } from '../../theme';
import { useGoogleLogin } from '@react-oauth/google';
import axios from "axios";
const baseURL = 'http://localhost:5000';

function Login() {

  const theme = useTheme();
  const colors = tokens(theme.palette.mode)

  const { user, setUser, logoutUser } = useContext(UserContext);
  const [googleUser, setGoogleUser] = useState(null);

  const login = useGoogleLogin({
    onSuccess: credentialResponse => setGoogleUser(credentialResponse),
    onError: err => console.log(err)
  });

  useEffect(
    () => {
      if (googleUser) {
        axios.get(`https://www.googleapis.com/oauth2/v1/userinfo?access_token=${googleUser.access_token}`, {
          headers: {
            Authorization: `Bearer ${googleUser.access_token}`,
            Accept: 'application/json'
          }
        })
          .then(res => {
            let userinfo = res.data
            axios.get(`${baseURL}/login/fetch_data`, { 'params': { 'email': res.data.email } })
              .then(response => {
                userinfo.pending_forms = response.data.pending_forms;
                console.log(userinfo);
                setUser(userinfo);
              })
              .catch(err => console.log(err.code))
            // TODO: get whether admin or not
          })
          .catch(err => console.log(err.data))
      }
    },
    [googleUser]
  );

  return (
    <>
      {user ? <Navigate to='/' /> : <></>}
      <Box
        display="flex"
        flexDirection="column"
        justifyContent="center"
        alignItems="center"
        height="50vh"
      >
        <Box>
          <Typography
            variant="h1"
            color={colors.grey[100]}
            fontWeight="bold"
            sx={{ mb: "5px " }}
          >
            Login</Typography>
        </Box>
        <br></br>
        <Box>
          <button onClick={login}> Sign in with Google </button>
        </Box>
      </Box>

    </>
  );
}

export default Login;
