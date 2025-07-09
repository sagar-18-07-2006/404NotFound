const calculateDistance = (lat1, lon1, lat2, lon2) => {
  const R = 6371; // Earth radius in km
  const dLat = toRad(lat2 - lat1);
  const dLon = toRad(lon2 - lon1);
  
  const a = 
    Math.sin(dLat/2) * Math.sin(dLat/2) +
    Math.cos(toRad(lat1)) * Math.cos(toRad(lat2)) * 
    Math.sin(dLon/2) * Math.sin(dLon/2);
    
  const c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
  return R * c; // Distance in km
};

const toRad = (value) => value * Math.PI / 180;

// Sort hospitals by distance
const sortByDistance = (hospitals, userLat, userLng) => {
  return hospitals.map(hospital => ({
    ...hospital._doc,
    distance: calculateDistance(
      userLat,
      userLng,
      hospital.location.coordinates[1],
      hospital.location.coordinates[0]
    )
  })).sort((a, b) => a.distance - b.distance);
};

module.exports = {
  calculateDistance,
  sortByDistance
};