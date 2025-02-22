import OrganizationChart from "../components/OrganizationChart";
import { Box, Typography } from "@mui/material";

const Dashboard = () => {
  return (
    <Box className="dashboard">
      <Typography
        variant="h5"
        sx={{
          textAlign: "center",
          fontWeight: "bold",
          textDecoration: "underline",
        }}
      >
        Organization Chart
      </Typography>
      <OrganizationChart />
    </Box>
  );
};

export default Dashboard;
