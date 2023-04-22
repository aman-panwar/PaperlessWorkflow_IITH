import { Routes, Route, useLocation, Navigate } from 'react-router-dom'
import Topbar from './pages/global/Topbar';
import Sidebar from './pages/global/Sidebar';
import Login from './pages/login';
import Home from './pages/home'
import Admin from './pages/admin';
import FAQ from './pages/FAQ';
import Form from './pages/form';
import Table from './pages/table';

// import Topbar from './Topbar'
import { ColorModeContext, useMode } from './theme'
import { CssBaseline, ThemeProvider } from '@mui/material'

function App() {
  const [theme, colorMode] = useMode()
  const location = useLocation();
  const isLogin = location.pathname.startsWith('/login');

  return(
    <>
    <ColorModeContext.Provider value={colorMode}>
      <ThemeProvider theme={theme}>
        <CssBaseline/>
          <div className='app'>
            {!isLogin ? <Sidebar/> : <></>} 
            <main className='content'>
              {!isLogin ? <Topbar/> : <></>}
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
    </>
  );
};

export default App

// function App() {
//   const [data, setData] = useState([{}])

//   useEffect(() => {
//     fetch("/contri").then(
//       res => res.json()
//     ).then(
//       data => {
//         setData(data)
//         console.log(data)
//       }
//     )
//   }, [])

//   const auth_sucess = (msg) => {
//     console.log("login success!")
//     console.log(msg);
//   };
//   const auth_fail = (msg) => {
//     console.log("login fail :(");
//     console.log(msg);
//   };

//   return (
//     <div>
//       <h1>project</h1>
//       {(typeof data.project == 'undefined') ? (
//         <p>loading...</p>
//       ) : (
//         <p>{data.project}</p>
//       )}

//       <h1>contributer</h1>
//       {(typeof data.contributer == 'undefined') ? (
//         <p>loading...</p>
//       ) : (
//         data.contributer.map((pers, i) => (
//           <p key={i}>{pers}</p>
//         ))
//       )}

//       <GoogleLogin onSuccess={auth_sucess} onError={auth_fail}/>
//     </div>
//   )
// }
