import UserPanel from "./components/UserPanel.jsx"
import './App.css'
import { useState } from "react"
function App() {
  const [fetchUser,setFetchUsers] = useState(false)
  return (
    <>
      <h1>Application Frontend</h1>
      <div className="gridmiecran" id="fetchUser">
      <button onClick={() => setFetchUsers(true)} disabled={fetchUser} > Recupérer les utilisateurs </button>
      </div>
      <div className="gridmiecran">
        {fetchUser === true ? <UserPanel/> : <></>}
      </div>
    </>
  )
}

export default App
