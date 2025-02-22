import { useEffect, useState } from "react";
import { Box, Stack, Typography } from "@mui/material";
import { DndContext, closestCorners } from "@dnd-kit/core";
import ManagerColumn from "./ManagerColumn";
import { get, patch } from "../utils/base";
import { showNotification } from "../utils/notification";
import { ToastContainer } from "react-toastify";

const OrganizationChart = () => {
  const [managers, setManagers] = useState([]);
  const [employees, setEmployees] = useState([]);
  const [loading, setLoading] = useState(true);

  const fetchData = async () => {
    try {
      const [managersRes, employeesRes] = await Promise.all([
        get("/manager"),
        get("/employee"),
      ]);

      if (!managersRes || !employeesRes) {
        throw new Error("Failed to fetch data");
      }

      setManagers(managersRes);
      setEmployees(employeesRes);
    } catch (error) {
      console.error("Error fetching data:", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleDragEnd = async (event) => {
    const { active, over } = event;

    if (!over) return;

    const employeeId = active.id;
    const newManagerId = over.id;

    // Find the employee that was dragged
    const draggedEmployee = employees.find(
      (emp) => emp.employee_id === employeeId
    );

    // If employee is dropped on the same manager, do nothing
    if (draggedEmployee?.manager.manager_id === newManagerId) return;

    try {
      // Make API call to update employee's manager
      const response = await patch(`/employee/${employeeId}/manager`, {
        manager_id: newManagerId,
      });

      if (!response) {
        throw new Error("Failed to update manager");
      }

      showNotification("success", "Employee's Manager Updated..!");
      fetchData();
    } catch (error) {
      console.log(error);
      showNotification(
        "error",
        error?.response?.data?.detail ?? "Employee's Manager Updation failed..!"
      );
      console.error("Error updating manager:", error);
    }
  };

  if (loading) {
    return (
      <Box sx={{ p: 3 }}>
        <Typography>Loading...</Typography>
      </Box>
    );
  }

  return (
    <DndContext onDragEnd={handleDragEnd} collisionDetection={closestCorners}>
      <Box
        sx={{
          width: "100%",
          overflowX: "auto",
          p: 3,
        }}
      >
        <Stack
          direction="row"
          spacing={3}
          sx={{
            minWidth: "min-content",
          }}
        >
          {managers.map((manager) => (
            <ManagerColumn
              key={manager.manager_id}
              manager={manager}
              employees={employees.filter(
                (emp) => emp.manager.manager_id === manager.manager_id
              )}
            />
          ))}
        </Stack>
      </Box>
      <ToastContainer />
    </DndContext>
  );
};

export default OrganizationChart;
