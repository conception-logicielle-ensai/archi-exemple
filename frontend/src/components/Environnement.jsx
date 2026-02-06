import { Paper, Typography, Stack } from "@mui/material";

const Environnement = () => {
  const environnement = import.meta.env.VITE_ENVIRONNEMENT;
  const apiUrl = import.meta.env.VITE_API_URL;

  return (
    <Paper sx={{ p: 4 }}>
      <Stack spacing={1}>
        <Typography>
          {"Environnement de déploiement :"} {environnement}
        </Typography>
        <Typography>
          {"URL d'API : "} {apiUrl}
        </Typography>
      </Stack>
    </Paper>
  );
};

export default Environnement;
