import React, { useState, useEffect, useContext } from "react";
import { Link } from "react-router-dom";

import { Context } from "../store/appContext";

export const Home = () => {
	const { store, actions } = useContext(Context);
	const [pet, setPet] = useState({ age: "", name: "", race: "", castrated: false });

	const createPet = async () => {
		const response = await fetch("https://3001-dedalovitor-cartsdv-kzvfvplsqkj.ws-eu86.gitpod.io/api/pet", {
			method: "POST",
			headers: {
				"content-Type": "application/json"
			},
			body: JSON.stringify()
		});
	}

	return (
		<div className="container">
			{store.currentUserEmail ?
				<div className="card w-25 p-3">
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
				</div> :
				"Please register or login"}
		</div >
	);

};
