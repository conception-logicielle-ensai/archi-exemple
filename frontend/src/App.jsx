import "./App.css";
import UserList from "./components/UserList";
import AddUserForm from "./components/AddUserForm";

import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";

function App() {
  return (
    <Router>
      <div className="container">
        <h1>Gestion des Utilisateurs</h1>
        <nav>
          <ul>
            <li>
              <Link to="/users/">Liste des utilisateurs</Link>
            </li>
            <li>
              <Link to="/users/add/">Ajouter un utilisateur</Link>
            </li>
          </ul>
        </nav>
        <Routes>
          <Route path="/users/" element={<UserList />} />
          <Route path="/users/add/" element={<AddUserForm />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
