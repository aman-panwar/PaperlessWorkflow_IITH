import React, { useState, createContext} from 'react'
import { Routes, Route, useLocation, Navigate } from 'react-router-dom'
import Topbar from './pages/global/Topbar';
import LoginTopbar from './pages/login/LoginTopbar'
import Sidebar from './pages/global/Sidebar';
import Login from './pages/login';
import Home from './pages/home'
import Admin from './pages/admin';
import FAQ from './pages/FAQ';
import Form from './pages/form';
import Table from './pages/table';

import { ColorModeContext, useMode } from './theme'
import { CssBaseline, ThemeProvider } from '@mui/material'

// const baseURL = 'http://localhost:5000';
export const UserContext = createContext();

function App() {

  const [theme, colorMode] = useMode()
  const location = useLocation();
  const isLogin = location.pathname.startsWith('/login');
  const [user, setUser] = useState(null);
  function logoutUser() {};

  return(
    <>
    <UserContext.Provider value={{user, setUser, logoutUser}}>
    <ColorModeContext.Provider value={colorMode}>
      <ThemeProvider theme={theme}>
        <CssBaseline/>
          <div className='app'>
            {!isLogin && user? <Sidebar/> : <></>} 
            <main className='content'>
              {!isLogin && user? <Topbar/> : <LoginTopbar/>}
                <Routes>
                    <Route path="/*" element={<Navigate to="/"/>} />
                    <Route path="/" element={<Home/>} />
                    <Route path="/admin" element={<Admin/>} />
                    <Route path="/FAQ" element={<FAQ/>} />
                    <Route path="/form" element={<Form/>} />
                    <Route path="/table" element={<Table/>} />

                    <Route path="/login" element={<Login/>} />
                </Routes>
            </main>
          </div>
      </ThemeProvider>
    </ColorModeContext.Provider>
    </UserContext.Provider>
    </>
  );

}

export default App;

