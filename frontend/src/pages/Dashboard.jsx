import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Topbar from '../scenes/global/Topbar';
import Sidebar from '../scenes/global/Sidebar';
import Admin from '../scenes/admin';
import FAQ from '../scenes/FAQ';
import Form from '../scenes/form';
import Home from '../scenes/home';
import Table from '../scenes/table';

function Dashboard() {

    return(
        <div className='app'>
            <Sidebar/>
            <main className='content'>
                <Topbar/>
                <Routes>
                    <Route path="/admin" element={<Admin/>} />
                    <Route path="/FAQ" element={<FAQ/>} />
                    <Route path="/form" element={<Form/>} />
                    <Route path="/home" element={<Home/>} />
                    <Route path="/table" element={<Table/>} />
                </Routes>
            </main>
        </div>
    );
}

export default Dashboard;