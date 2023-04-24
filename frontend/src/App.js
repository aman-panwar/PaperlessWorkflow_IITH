import React, { useState, useEffect } from 'react'
import { googleLogout, useGoogleLogin } from '@react-oauth/google';
import axios from "axios";
const baseURL = 'http://localhost:5000'

function App() {
 // const [data, setData] = useState([{}])
  //
  // useEffect(() => {
  //   fetch("/contri").then(
  //     res => res.json()
  //   ).then(
  //     data => {
  //       setData(data)
  //       console.log(data)
  //     }
  //   )
  // }, [])
  //
  // const auth_sucess = async (credentialResponse) => {
  //   console.log("login success!")
  //   console.log(credentialResponse);
  //   const userInfo = await axios.get(`${baseURL}/auth/get_creds`, { params : credentialResponse})
  //   .then(response => console.log(response.data))
  //   .catch(err => console.log(err));
  //
  //   console.log(userInfo);
  // };
  // const auth_fail = (msg) => {
  //   console.log("login fail :(");
  //   console.log(msg);
  // };
  //
  // return (
  //   <div>
  //     <h1>project</h1>
  //     {(typeof data.project == 'undefined') ? (
  //       <p>loading...</p>
  //     ) : (
  //       <p>{data.project}</p>
  //     )}
  //
  //     <h1>contributer</h1>
  //     {(typeof data.contributer == 'undefined') ? (
  //       <p>loading...</p>
  //     ) : (
  //       data.contributer.map((pers, i) => (
  //         <p key={i}>{pers}</p>
  //       ))
  //     )}
  //
  //     <GoogleLogin onSuccess={auth_sucess} onError={auth_fail}/>
  //   </div>
  // )

  const [user, setUser] = useState([]);
  const [profile, setProfile] = useState([]);

  const login = useGoogleLogin({
    onSuccess: credentialResponse => setUser(credentialResponse),
    onError: err => console.log(err)
  });

  useEffect(
    () => {
      if (user) {
        axios.get(`https://www.googleapis.com/oauth2/v1/userinfo?access_token=${user.access_token}`, {
          headers: {
            Authorization: `Bearer ${user.access_token}`,
            Accept: 'application/json'
          }
        })
        .then(res => {
            console.log(res.data);
            setProfile(res.data);
          })
        .catch(err => console.log(err.data))
      }
    },
    [ user ]
  );

  const logout = () => {
    googleLogout();
    setProfile(null);
  }

  return (
    <div>
      <h2>Google Login</h2>
      <br />
      <br />
      {profile ? (
        <div>
          <img src={profile.picture} alt="user profile pic" />
          <h3> User Logged In </h3>
          <p>Name: {profile.name}</p>
          <p>Email: {profile.email}</p>
          <br />
          <br />
          <button onClick={logout}> Log Out </button>
        </div>
      ) : (
        <button onClick={login}> Sign in with Google </button>
      )}
    </div>
  );

}

export default App
