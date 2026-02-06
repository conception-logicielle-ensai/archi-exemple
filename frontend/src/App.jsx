import { BrowserRouter, Routes, Route } from "react-router-dom";

import Header from "./styles/Header";
import AppLayout from "./styles/AppLayout";

import UserList from "./components/UserList";
import AddUserForm from "./components/AddUserForm";
import Environnement from "./components/Environnement";

function App() {
  return (
    <BrowserRouter>
      <Header />
      <AppLayout>
        <Routes>
          <Route path="/users" element={<UserList />} />
          <Route path="/add-user" element={<AddUserForm />} />
          <Route path="/env" element={<Environnement />} />
        </Routes>
      </AppLayout>
    </BrowserRouter>
  );
}

export default App;
