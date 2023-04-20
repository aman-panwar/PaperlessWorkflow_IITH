import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Dashboard from './pages/Dashboard'
import Login from './pages/Login'
import Navbar from './Navbar'

function App() {
  return(
    <>
    <BrowserRouter>
      <Routes>
        <Route exact path='/' element={<Dashboard />}/>
        <Route exact path='/login' element={<Login navbar={<Navbar/>}/>}/>
      </Routes>
    </BrowserRouter>
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
