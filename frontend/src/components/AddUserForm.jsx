import { useState } from "react";
import "../styles/AddUserForm.css";
import API from "../api/apiClient.js";

function AddUserForm() {
  const [username, setUsername] = useState("");
  const [roles, setRoles] = useState("");

  const addUser = async (username, roles) => {
    if (!username.trim()) {
      alert("Le nom d'utilisateur ne peut pas être vide.");
      return;
    }
    if (!roles.length) {
      alert("L'utilisateur doit avoir au moins un rôle.");
      return;
    }

    try {
      await API.post(`/users/?username=${username}`, roles, {
        headers: {
          "Content-Type": "application/json",
        },
      });
    } catch (error) {
      alert("Une erreur est survenue lors de l'ajout de l'utilisateur.");
      console.error("Erreur lors de l'ajout de l'utilisateur", error);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const rolesArray = roles.split(",").map((role) => role.trim());
    addUser(username, rolesArray);
    setUsername("");
    setRoles("");
  };

  return (
    <form onSubmit={handleSubmit} className="add-user-form">
      <input
        type="text"
        placeholder="Nom d'utilisateur"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        required
      />
      <input
        type="text"
        placeholder="Rôles (séparés par des virgules)"
        value={roles}
        onChange={(e) => setRoles(e.target.value)}
        required
      />
      <button type="submit">Ajouter Utilisateur</button>
    </form>
  );
}

export default AddUserForm;
