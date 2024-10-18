import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Home from './components/Home';
import Contact from './components/Contact';
import KnowMore from './components/KnowMore';
import Login from './components/Login';
import CloakFeature from './components/CloakFeature';
import './components/App.css'; 

function App() {
  return (
    <Router>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/contact">Contact</Link></li>
          <li><Link to="/know-more">Know More</Link></li>
          <li><Link to="/login">Login</Link></li>
          <li><Link to="/cloak">Activate Cloak</Link></li>
        </ul>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/contact" element={<Contact />} />
        <Route path="/know-more" element={<KnowMore />} />
        <Route path="/login" element={<Login />} />
        <Route path="/cloak" element={<CloakFeature />} />
      </Routes>
    </Router>
  );
}

export default App;
