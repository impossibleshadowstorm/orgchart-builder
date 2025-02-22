import { Card, CardContent, Typography, Box, Paper } from "@mui/material";

const ProfileCard = ({ name, email, department, manager = false }) => {
  return (
    <Card
      sx={{
        maxWidth: 400,
        width: "100%",
        margin: "auto",
        bgcolor: "rgba(255, 255, 255, 0.8)",
        backdropFilter: "blur(8px)",
        transition: "all 0.3s ease",
        cursor: manager ? "" : "grab",
        zIndex: "100 !important",
        ...(!manager && {
          "&:hover": {
            boxShadow: 6,
          },
        }),
      }}
    >
      <CardContent>
        <Box
          sx={{
            display: "flex",
            flexDirection: "column",
            alignItems: "center",
            gap: 2,
            py: 2,
          }}
        >
          <Box sx={{ textAlign: "center" }}>
            {manager && (
              <Paper
                elevation={0}
                sx={{
                  display: "inline-block",
                  px: 1.5,
                  py: 0.5,
                  borderRadius: 10,
                  bgcolor: "rgba(0, 0, 0, 0.04)",
                  mb: 1,
                }}
              >
                <Typography variant="caption" color="text.secondary">
                  {department}
                </Typography>
              </Paper>
            )}
            <Typography
              variant="h5"
              component="h3"
              sx={{ fontWeight: 600, mb: 0.5 }}
            >
              {name}
            </Typography>
            <Typography
              variant="body2"
              color="text.secondary"
              sx={{
                "&:hover": {
                  transition: "color 0.2s ease",
                },
              }}
            >
              {email}
            </Typography>
          </Box>
        </Box>
      </CardContent>
    </Card>
  );
};

export default ProfileCard;
