import { useState } from "react";
import UserCard from "./UserCard";
import "../styles/UserList.css";
import API from "../api/apiClient.js";

function UserList() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(false);

  const fetchUsers = async () => {
    setLoading(true);
    try {
      const response = await API.get("/users/");
      setUsers(response.data);
    } catch (error) {
      alert("Erreur lors de la récupération des utilisateurs :", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="user-list">
      <button onClick={fetchUsers}>Récupérer les utilisateurs</button>
      {loading && <p>Chargement...</p>}
      <div className="users-container">
        {users.length > 0 &&
          users.map((user) => <UserCard key={user.id} user={user} />)}
      </div>
    </div>
  );
}

export default UserList;
