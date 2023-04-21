import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom'
import Dashboard from './pages/Dashboard'
import Login from './pages/Login'
import Navbar from './Navbar'
import { ColorModeContext, useMode } from './theme'
import { CssBaseline, ThemeProvider } from '@mui/material'

function App() {
  const [theme, colorMode] = useMode()
  return(
    <>
    <ColorModeContext.Provider value={colorMode}>
      <ThemeProvider theme={theme}>
        <CssBaseline/>
          <BrowserRouter>
            <Routes>
              <Route path='/*' element={<Navigate to="/"/>} />
              <Route exact path='/' element={<Dashboard />}/>
              <Route exact path='/login' element={<Login navbar={<Navbar/>}/>}/>
            </Routes>
          </BrowserRouter>
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
