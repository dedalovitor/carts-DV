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
		const response = await fetch("https://3001-dedalovitor-cartsdv-kzvfvplsqkj.ws-eu86.gitpod.io/api/pets");
		const data = await response.json();
		setPets(data.results)
	}

	const createPet = async () => {
		const response = await fetch("https://3001-dedalovitor-cartsdv-kzvfvplsqkj.ws-eu86.gitpod.io/api/pet", {
			method: "POST",
			headers: {
				"content-Type": "application/json",
				"Authorization": "Bearer " + localStorage.getItem("token")
			},
			body: JSON.stringify(pet)
		});
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
						{pets.map((pet) => {
							return <div class="card" style="width: 18rem;">
								<img src="..." class="card-img-top" alt="..." />
								<div class="card-body">
									<h5 class="card-title">Card title</h5>
									<p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
									<a href="#" class="btn btn-primary">Go somewhere</a>
								</div>
							</div>
						})}

					</div>
				</> :
				"Please register or login"}
		</div >
	);

};
