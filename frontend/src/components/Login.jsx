
import './App.css';

function Login() {
  return (
    <div className="container">
      <h1>Login</h1>
      <form>
        <label>Username: </label>
        <input type="text" name="username" />
        <br />
        <label>Password: </label>
        <input type="password" name="password" />
        <br />
        <button type="submit">Login</button>
      </form>
    </div>
  );
}

export default Login;
