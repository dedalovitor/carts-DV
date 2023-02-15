import React, { useState, useEffect, useContext } from "react";
import { Link } from "react-router-dom";

import { Context } from "../store/appContext";

export const Home = () => {
	const { store, actions } = useContext(Context);
	const [pet, setPet] = useState({ age: "", name: "", race: "", castrated: false });
	const [pets, setPets] = useState([]);

	useEffect(() => {
		getCurrentUserPets();
	}, [])

	const getCurrentUserPets = async () => {
		const response = await fetch(process.env.BACKEND_URL + "/api/pets", {
			method: "GET",
			headers: {
				"content-Type": "application/json",
				"Authorization": "Bearer " + localStorage.getItem("token")
			}
		});
		const data = await response.json();
		setPets(data.results);
	}

	const createPet = async () => {
		const response = await fetch(process.env.BACKEND_URL + "/api/pet", {
			method: "POST",
			headers: {
				"content-Type": "application/json",
				"Authorization": "Bearer " + localStorage.getItem("token")
			},
			body: JSON.stringify(pet)
		});
		if (response.ok) getCurrentUserPets();
	}

	const deletePet = async (id) => {
		const response = await fetch(process.env.BACKEND_URL + "/api/pet/" + id, {
			method: "DELETE",
			headers: {
				"content-Type": "application/json",
				"Authorization": "Bearer " + localStorage.getItem("token")
			}
		});
		if (response.ok) getCurrentUserPets();
	}


	return (
		<div className="container">
			{store.currentUserEmail ?
				<>
					<div className="card COL-5 w-25 p-3">
						{Object.keys(pet).map((key, i) => {
							if (typeof pet[key] != "boolean") {
								return <input placeholder={key} key={i} name={key} defaultValue={pet[key]}
									onChange={(e) => setPet({ ...pet, [key]: e.target.value })}>
								</input>
							} else {
								return <input type="checkbox" key={i} name={key} checked={pet[key]}
									onChange={(e) => setPet({ ...pet, [key]: e.target.checked })}>
								</input>
							}

						})}
						<button className="btn btn-success" onClick={() => createPet()}>CREATE PET</button>
					</div>

					<div className="row">
						{pets.map((x) => {
							return <div key={x.id} className="card" style={{ width: "18rem" }}>
								<img className="card-img-top" src="https://www.cdc.gov/healthypets/images/pets/angry-dog.jpg?_=03873" alt="Card image cap" />
								<div className="card-body">
									<p className="card-text"> age: {x.age} </p>
									<p className="card-text"> name: {x.name} </p>
									<p className="card-text"> race: {x.race} </p>
									castrated: <input type="checkbox" disabled className="card-text" checked={x.castrated} />
								</div>
								<div className="card-footer">
									<button className="btn btn-danger" onClick={() => deletePet(x.id)}>DEL</button>
								</div>
							</div>
						})}

					</div>
				</> :
				"Please register or login"}
		</div >
	);

};
