import React, { useState } from "react";
import LoginPage from "./components/pages/LoginPage";

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);

  return (
    <div>
      <h1>Welcome to the Event Management System</h1>
      <LoginPage setIsLoggedIn={setIsLoggedIn} />
    </div>
  );
}

export default App;
