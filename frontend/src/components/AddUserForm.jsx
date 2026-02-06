import { useState } from "react";
import { Paper, Typography, Stack, TextField, Button } from "@mui/material";

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
      await API.post("/users/", {
        username,
        roles: roles.split(",").map((r) => r.trim()),
      });
      setUsername("");
      setRoles("");
    } catch {
      alert("Erreur lors de l'ajout de l'utilisateur.");
    }
  };

  return (
    <Paper sx={{ p: 4, maxWidth: 500 }}>
      <Typography variant="h6" mb={2}>
        Ajouter un utilisateur
      </Typography>

      <Stack
        component="form"
        spacing={2}
        onSubmit={(e) => {
          e.preventDefault();
          addUser(username, roles);
        }}
      >
        <TextField
          label="Nom d'utilisateur"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          fullWidth
        />

        <TextField
          label="Rôles (séparés par des virgules)"
          value={roles}
          onChange={(e) => setRoles(e.target.value)}
          fullWidth
        />

        <Button type="submit" variant="contained">
          Ajouter
        </Button>
      </Stack>
    </Paper>
  );
}

export default AddUserForm;
