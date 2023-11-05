import { initializeApp } from "firebase/app";
import { getFirestore } from "firebase/firestore";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "AIzaSyC8_oMQFrnDigchq7cpYiKdYCO4ddmhoCU",
  authDomain: "claude-career-compass.firebaseapp.com",
  projectId: "claude-career-compass",
  storageBucket: "claude-career-compass.appspot.com",
  messagingSenderId: "155147357253",
  appId: "1:155147357253:web:e57fc16dd7fcefd7c5e72c"
};

const app = initializeApp(firebaseConfig);

const auth = getAuth(app);

export default auth;