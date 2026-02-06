import { useState } from "react";
import {
  Paper,
  Typography,
  Stack,
  Button,
  CircularProgress,
} from "@mui/material";

import UserCard from "./UserCard";
import API from "../api/apiClient.js";

function UserList() {
  const [users, setUsers] = useState([]);
  const [loading, setLoading] = useState(false);

  const fetchUsers = async () => {
    setLoading(true);
    try {
      const response = await API.get("/users/");
      setUsers(response.data);
    } catch {
      alert("Erreur lors de la récupération des utilisateurs.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Paper sx={{ p: 4 }}>
      <Stack
        direction="row"
        justifyContent="space-between"
        alignItems="center"
        mb={3}
      >
        <Typography variant="h6">Liste des utilisateurs</Typography>

        <Button variant="contained" onClick={fetchUsers}>
          Récupérer les utilisateurs
        </Button>
      </Stack>

      {loading && <CircularProgress />}

      <Stack spacing={2}>
        {users.map((user) => (
          <UserCard key={user.id} user={user} />
        ))}
      </Stack>
    </Paper>
  );
}

export default UserList;
