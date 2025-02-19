import "../styles/UserCard.css";
import PropTypes from "prop-types";

function UserCard({ user }) {
  return (
    <div className="user-card">
      <h2>{user.username}</h2>
      <p>ID: {user.id}</p>
      <p>Rôles: {user.roles.join(", ")}</p>
    </div>
  );
}

UserCard.propTypes = {
  user: PropTypes.shape({
    username: PropTypes.string.isRequired,
    id: PropTypes.number.isRequired,
    roles: PropTypes.arrayOf(PropTypes.string).isRequired,
  }).isRequired,
};

export default UserCard;
