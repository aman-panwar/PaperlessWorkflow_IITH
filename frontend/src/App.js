import React, {useState, useEffect}  from 'react'

function App(){
  const [data, setData] = useState([{}])

  useEffect(() => {
      fetch("/contri").then(
        res => res.json()
      ).then(
        data=>{
          setData(data)
          console.log(data)
        }
      )
  }, [])

  return (
    <div>
      <h1>project</h1>
      {(typeof data.project == 'undefined')?(
        <p>loading...</p>
      ):(
        <p>{data.project}</p>
      )}

    <h1>contributer</h1>
      {(typeof data.contributer == 'undefined')?(
        <p>loading...</p>
      ):(
        data.contributer.map((pers, i) => (
            <p key={i}>{pers}</p>
          )) 
      )}

    </div>
  )
}

export default App