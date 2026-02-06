import { AppBar, Toolbar, Typography, Box, Button } from "@mui/material";
import { NavLink } from "react-router-dom";

export default function Header() {
  return (
    <AppBar position="static" color="default">
      <Toolbar sx={{ justifyContent: "space-between" }}>
        <Typography variant="h6" fontWeight={600}>
          Gestion des utilisateurs
        </Typography>

        <Box sx={{ display: "flex", gap: 2 }}>
          <Button component={NavLink} to="/users">
            Utilisateurs
          </Button>
          <Button component={NavLink} to="/add-user">
            Ajouter
          </Button>
          <Button component={NavLink} to="/env">
            Environnement
          </Button>
        </Box>
      </Toolbar>
    </AppBar>
  );
}
