import { Box, Stack } from "@mui/material";
import { useDroppable } from "@dnd-kit/core";
import ProfileCard from "./ProfileCard";
import DraggableEmployee from "./DraggableEmployee";

const ManagerColumn = ({ manager, employees }) => {
  const { setNodeRef } = useDroppable({
    id: manager.manager_id,
  });

  return (
    <Box
      ref={setNodeRef}
      sx={{
        p: 2,
        minWidth: 320,
        height: "100%",
        bgcolor: "rgba(52, 51, 51, 0.8)",
        backdropFilter: "blur(8px)",
        transition: "background-color 0.2s ease",
        zIndex: 0,
      }}
    >
      <Box sx={{ mb: 3 }}>
        <ProfileCard
          name={`${manager.first_name} ${manager.last_name}`}
          email={manager.email}
          department={manager.department}
          manager={true}
        />
      </Box>
      <Stack spacing={2}>
        {employees.map((employee) => (
          <DraggableEmployee key={employee.employee_id} employee={employee} />
        ))}
      </Stack>
    </Box>
  );
};

export default ManagerColumn;
