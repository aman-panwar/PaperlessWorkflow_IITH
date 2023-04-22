import React, { useState, useEffect } from 'react'
import { GoogleLogin } from '@react-oauth/google';
// import Topbar from '../Topbar'

function Login() {
    const auth_success = (message) => {console.log('Successful login')}
    const auth_fail = (message) => {console.log('Login Failed')}

    return(
        <>
        <h1>This is the Login page</h1>
        <GoogleLogin onSuccess={auth_success} onError={auth_fail}/>
        </>
    );
}

export default Login;