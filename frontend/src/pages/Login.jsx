// import Form from "../components/FormLogin"
import Form from "../components/LoginForm"

function Login() {
    return (
        <div>
            <Form route="/api/token/" method="login" />
        </div>
    )
}

export default Login