import { Box, Container } from "@mui/material";
import PropTypes from "prop-types";

export default function AppLayout({ children }) {
  return (
    <Box sx={{ minHeight: "100vh", display: "flex", flexDirection: "column" }}>
      <Container maxWidth="lg" sx={{ flex: 1, py: 4 }}>
        {children}
      </Container>
    </Box>
  );
}

AppLayout.propTypes = {
  children: PropTypes.node.isRequired,
};
