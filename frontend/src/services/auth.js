export const loginUser = async (username, password) => {
    try {
      const response = await axios.post('http://localhost:8000/api/token/', {
        username,
        password,
      });
      const token = response.data.access;
      localStorage.setItem('token', token);
      return token;
    } catch (error) {
      console.error('Login failed', error);
      throw error;
    }
  };
  
  export const getToken = () => {
    return localStorage.getItem('token');
  };
  
  export const isAuthenticated = () => {
    return !!getToken(); // Si un token existe, l'utilisateur est connecté
  };
  