const mongoose = require('mongoose');

const DoctorSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true
    },
    specialty: {
        type: String,
        required: true
    },
    hospital: {
        type: mongoose.Schema.Types.ObjectId,
        ref: 'Hospital',
        required: true
    },
    schedule: [{
        day: {
            type: String,
            enum: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
            required: true
        },
        startTime: String,
        endTime: String,
        slots: [String] // e.g., ["09:00", "09:30", "10:00"]
    }],
    rating: {
        type: Number,
        default: 0
    },
    symptoms: [String] // symptoms this doctor specializes in
});

module.exports = mongoose.model('Doctor', DoctorSchema);