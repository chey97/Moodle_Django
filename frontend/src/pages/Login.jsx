// import Form from "../components/FormLogin"
import Form from "../components/LoginForm"
import Navigation from "../components/Navigation"
import SideImage from "../components/SideImage"

function Login() {
    return (
        <div>
            <Form route="/api/token/" method="login" />
        </div>
    )
}

export default Login