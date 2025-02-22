import { toast } from "react-toastify";

export const showNotification = (type, message, duration = 5000) => {
  toast[type.toLowerCase()](message, {
    position: "top-right",
    autoClose: duration,
    closeOnClick: true,
  });
};
