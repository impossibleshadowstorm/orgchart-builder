import { useDraggable } from "@dnd-kit/core";
import ProfileCard from "./ProfileCard";

const DraggableEmployee = ({ employee }) => {
  const {
    attributes,
    listeners,
    setNodeRef,
    transform,
    isDragging,
  } = useDraggable({
    id: employee.employee_id,
  });

  const style = transform
    ? {
        transform: `translate3d(${transform.x}px, ${transform.y}px, 0)`,
        zIndex: isDragging ? 999 : 100,
        opacity: isDragging ? 1 : undefined,
        cursor: "grab",
      }
    : undefined;

  return (
    <div ref={setNodeRef} style={style} {...listeners} {...attributes}>
      <ProfileCard
        name={`${employee.first_name} ${employee.last_name}`}
        email={employee.email}
        department={employee.department}
      />
    </div>
  );
};

export default DraggableEmployee;
