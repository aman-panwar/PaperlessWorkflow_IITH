import React, { useState, useEffect } from 'react'
import { GoogleLogin } from '@react-oauth/google';
import { Navigate } from 'react-router-dom';

import { Box, useTheme, Typography } from '@mui/material';
import { tokens } from '../../theme';

function Login() {

    const theme = useTheme();
    const colors = tokens(theme.palette.mode)
    const [authenticated, setAuthenticated] = useState(false);

    const auth_success = (message) => {
        console.log('Successful login');
        setAuthenticated(true);

    }
    const auth_fail = (message) => {
        console.log('Login Failed');
        setAuthenticated(false);
    }

    if(authenticated){
        return <Navigate to='/'/>
    }

    

    return(
        <>
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
                sx ={{ mb: "5px "}}
                >
                    Login</Typography>
            </Box>
            <br></br>
            <Box>
            <GoogleLogin onSuccess={auth_success} onError={auth_fail}/>
            </Box> 
        </Box>
        
        </>
    );
}

export default Login;