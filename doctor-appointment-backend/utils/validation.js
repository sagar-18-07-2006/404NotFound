const { check, validationResult } = require('express-validator');

// Common validation rules
const userValidationRules = () => [
  check('email').isEmail().normalizeEmail(),
  check('password').isLength({ min: 6 }),
  check('name').not().isEmpty().trim()
];

const appointmentValidationRules = () => [
  check('doctorId').isMongoId(),
  check('date').isISO8601(),
  check('symptoms').isArray({ min: 1 })
];

// Format validation errors
const validate = (req, res, next) => {
  const errors = validationResult(req);
  if (errors.isEmpty()) return next();

  const extractedErrors = errors.array().map(err => ({
    [err.param]: err.msg
  }));

  return res.status(422).json({
    errors: extractedErrors
  });
};

module.exports = {
  userValidationRules,
  appointmentValidationRules,
  validate
};