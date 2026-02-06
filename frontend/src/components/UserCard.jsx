import PropTypes from "prop-types";
import { Card, CardContent, Typography, Stack } from "@mui/material";

function UserCard({ user }) {
  return (
    <Card>
      <CardContent>
        <Stack spacing={0.5}>
          <Typography variant="h6">{user.username}</Typography>

          <Typography color="text.secondary">ID : {user.id}</Typography>

          <Typography>Rôles : {user.roles.join(", ")}</Typography>
        </Stack>
      </CardContent>
    </Card>
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
