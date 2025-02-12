import React from "react"
import axios from 'axios';

function UserPanel(){
    const [user,setUsers]=React.useState([])
    const fetchUsersOnRender = React.useEffect(() =>{
        const fetchData = async () =>{
            try {
              const {data: response} = await axios.get('/stuff/to/fetch');
              setData(response);
            } catch (error) {
              console.error(error.message);
            }
            setLoading(false);
          }})
    return <div>user</div>
}

export default UserPanel
