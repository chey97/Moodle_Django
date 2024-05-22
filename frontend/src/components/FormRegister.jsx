import { useState } from "react";
import api from "../api";
import { useNavigate } from "react-router-dom";
import "../styles/Form.css";
import LoadingIndicator from "./LoadingIndicator";

function RegisterForm({ route }) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [email, setEmail] = useState("");
    const [firstName, setFirstName] = useState("");
    const [lastName, setLastName] = useState("");
    const [role, setRole] = useState("");
    const [contactNo, setContactNo] = useState("");
    const [contactPerson, setContactPerson] = useState(""); // For student
    const [classroom, setClassroom] = useState(""); // For student
    const [dateOfBirth, setDateOfBirth] = useState(""); // For student
    const [loading, setLoading] = useState(false);
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        setLoading(true);
        e.preventDefault();

        if (password !== confirmPassword) {
            alert("Passwords do not match!");
            setLoading(false);
            return;
        }

        const userData = {
            username,
            password,
            email,
            first_name: firstName,
            last_name: lastName,
            role,
            contact_no: contactNo
        };

        if (role === "student") {
            userData.contact_person = contactPerson;
            userData.classroom = parseInt(classroom, 10); // Ensure classroom is an integer
            userData.date_of_birth = dateOfBirth;
        }

        try {
            await api.post(route, userData);
            navigate("/login");
        } catch (error) {
            alert(error);
        } finally {
            setLoading(false);
        }
    };

    return (
        <form onSubmit={handleSubmit} className="form-container">
            <h1>Register</h1>
            <div className="form-grid">
                <input
                    className="form-input"
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    placeholder="Username"
                    required
                />
                <input
                    className="form-input"
                    type="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="Email"
                    required
                />
                <input
                    className="form-input"
                    type="text"
                    value={firstName}
                    onChange={(e) => setFirstName(e.target.value)}
                    placeholder="First Name"
                    required
                />
                <input
                    className="form-input"
                    type="text"
                    value={lastName}
                    onChange={(e) => setLastName(e.target.value)}
                    placeholder="Last Name"
                    required
                />
                <select
                    className="form-input"
                    value={role}
                    onChange={(e) => setRole(e.target.value)}
                    required
                >
                    <option value="student">Student</option>
                    <option value="administrator">Administrator</option>
                    <option value="teacher">Teacher</option>
                </select>
                <input
                    className="form-input"
                    type="text"
                    value={contactNo}
                    onChange={(e) => setContactNo(e.target.value)}
                    placeholder="Contact No"
                    required
                />
                {role === "student" && (
                    <>
                        <input
                            className="form-input"
                            type="text"
                            value={contactPerson}
                            onChange={(e) => setContactPerson(e.target.value)}
                            placeholder="Contact Person"
                            required
                        />
                        <input
                            className="form-input"
                            type="number"
                            value={classroom}
                            onChange={(e) => setClassroom(e.target.value)}
                            placeholder="Classroom"
                            required
                        />
                        <input
                            className="form-input"
                            type="date"
                            value={dateOfBirth}
                            onChange={(e) => setDateOfBirth(e.target.value)}
                            placeholder="Date of Birth"
                            required
                        />
                    </>
                )}
                <input
                    className="form-input"
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Password"
                    required
                />
                <input
                    className="form-input"
                    type="password"
                    value={confirmPassword}
                    onChange={(e) => setConfirmPassword(e.target.value)}
                    placeholder="Confirm Password"
                    required
                />
            </div>
            {loading && <LoadingIndicator />}
            <button className="form-button" type="submit">
                Register
            </button>
        </form>
    );
}

export default RegisterForm;
