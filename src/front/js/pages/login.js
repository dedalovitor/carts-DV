import React, { useContext, useState } from "react";
import { Context } from "../store/appContext";
import { useNavigate } from "react-router-dom";

export const Login = () => {
	const navigate = useNavigate();
	const { store, actions } = useContext(Context);
	const [email, setEmail] = useState("");
	const [password, setPassword] = useState("");
	const [error, setError] = useState(false);

	const sendLoginCredential = async () => {
		const response = await fetch("https://3001-dedalovitor-authenticat-lembko6r0py.ws-eu86.gitpod.io/api/login", {
			method: "POST",
			headers: {
				"content-Type": "application/json"
			},
			body: JSON.stringify({
				email: email,
				password: password,
			})
		});
		if (response.ok) {
			const data = await response.json();
			localStorage.setItem("token", data.token);
			await actions.getCurrentUserEmail();
			navigate("/");
		} else {
			setError(true)
		}


	}

	return (
		<div className="text-center mt-5">
			LOGIN
			<div>
				<div>
					<label htmlFor="email">Email</label>
					<input name="email" placeholder="email" value={email} onChange={(e) => {
						setError(false);
						setEmail(e.target.value);
					}
					}></input>
				</div>
				<div>
					<label htmlFor="password">Password</label>
					<input name="password" placeholder="password" value={password} onChange={(e) => {
						setError(false);
						setPassword(e.target.value);
					}
					}></input>
				</div>
				<button className="btn btn-primary" onClick={() => sendLoginCredential()}>Login</button>
				{error ? <p className="alert alert-danger">Error en credenciales</p> : null}
			</div>
		</div>
	);
};
