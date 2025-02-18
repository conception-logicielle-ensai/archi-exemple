import React from "react";
import "../styles/UserCard.css";

function UserCard({ user }) {
  return (
    <div className="user-card">
      <h2>{user.username}</h2>
      <p>ID: {user.id}</p>
      <p>Rôles: {user.roles.join(", ")}</p>
    </div>
  );
}

export default UserCard;
