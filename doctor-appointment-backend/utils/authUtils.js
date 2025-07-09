const jwt = require('jsonwebtoken');
const config = require('config');

// Generate JWT token
const generateToken = (userId) => {
  return jwt.sign(
    { userId },
    config.get('jwtSecret'),
    { expiresIn: '1h' }
  );
};

// Verify JWT token
const verifyToken = (token) => {
  try {
    return jwt.verify(token, config.get('jwtSecret'));
  } catch (err) {
    throw new Error('Invalid token');
  }
};

// Extract token from request headers
const getTokenFromHeader = (req) => {
  const authHeader = req.headers.authorization;
  if (authHeader && authHeader.startsWith('Bearer ')) {
    return authHeader.split(' ')[1];
  }
  return null;
};

module.exports = {
  generateToken,
  verifyToken,
  getTokenFromHeader
};