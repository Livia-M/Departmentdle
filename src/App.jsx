/* Copyright (C) Livia Muamba - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Written by Livia Muamba, November 2025 */

App.jsx

import { useState, useEffect } from 'react'
import './App.css'
import './css/style.css'
import { Autocomplete } from '@mui/material';
import { TextField } from '@mui/material';

import Attempts from './components/Attempts.jsx';
import Constants from './constants/Constants.jsx';

function App() {
	const APEX_LABEL = "Point culminant";
	const DEPARTMENT_LABEL = "Département";
	const DEPARTMENTS_LABEL = "Départements";
	const DISTANCE_LABEL = "Distance";
	const EAST_WEST_LABEL = "Est / Ouest";
	const NORTH_SOUTH_LABEL = "Nord / Sud";
	const PREFECTURE_LABEL = "Préfecture";
	const PREFECTURE_POP_LABEL = "Pop. préfecture"
	const REGION_LABEL = "Région";
	const SEAS_OCEANS_LABEL = "Mers et Océans";
	const TEL_AREA_CODE_LABEL = "Indicatif tél.";

	const [guess, setGuess] = useState("");
	const [result, setResult] = useState("");
    const [whole, setWhole] = useState([]);
    const [clientKey, setClientKey] = useState("");
    const [gameWon, setGameWon] = useState(false);
    const [attemptCount, setAttemptCount] = useState(0);

	let fullDepartmentNames = ["01 - Ain", "02 - Aisne", "03 - Allier", "04 - Alpes-de-Haute-Provence", "05 - Hautes-Alpes", "06 - Alpes-Maritimes", "07 - Ardèche", "08 - Ardennes", "09 - Ariège", "10 - Aube", "11 - Aude", "12 - Aveyron", "13 - Bouches-du-Rhône", "14 - Calvados", "15 - Cantal", "16 - Charente", "17 - Charente-Maritime", "18 - Cher", "19 - Corrèze", "2A - Corse-du-Sud", "2B - Haute-Corse", "21 - Côte-d'Or", "22 - Côtes-d'Armor", "23 - Creuse", "24 - Dordogne", "25 - Doubs", "26 - Drôme", "27 - Eure", "28 - Eure-et-Loir", "29 - Finistère", "30 - Gard", "31 - Haute-Garonne", "32 - Gers", "33 - Gironde", "34 - Hérault", "35 - Ille-et-Vilaine", "36 - Indre", "37 - Indre-et-Loire", "38 - Isère", "39 - Jura", "40 - Landes", "41 - Loir-et-Cher", "42 - Loire", "43 - Haute-Loire", "44 - Loire-Atlantique", "45 - Loiret", "46 - Lot", "47 - Lot-et-Garonne", "48 - Lozère", "49 - Maine-et-Loire", "50 - Manche", "51 - Marne", "52 - Haute-Marne", "53 - Mayenne", "54 - Meurthe-et-Moselle", "55 - Meuse", "56 - Morbihan", "57 - Moselle", "58 - Nièvre", "59 - Nord", "60 - Oise", "61 - Orne", "62 - Pas-de-Calais", "63 - Puy-de-Dôme", "64 - Pyrénées-Atlantiques", "65 - Hautes-Pyrénées", "66 - Pyrénées-Orientales", "67 - Bas-Rhin", "68 - Haut-Rhin", "69 - Rhône", "70 - Haute-Saône", "71 - Saône-et-Loire", "72 - Sarthe", "73 - Savoie", "74 - Haute-Savoie", "75 - Paris", "76 - Seine-Maritime", "77 - Seine-et-Marne", "78 - Yvelines", "79 - Deux-Sèvres", "80 - Somme", "81 - Tarn", "82 - Tarn-et-Garonne", "83 - Var", "84 - Vaucluse", "85 - Vendée", "86 - Vienne", "87 - Haute-Vienne", "88 - Vosges", "89 - Yonne", "90 - Territoire de Belfort", "91 - Essonne", "92 - Hauts-de-Seine", "93 - Seine-Saint-Denis", "94 - Val-de-Marne", "95 - Val-d'Oise", "971 - Guadeloupe", "972 - Martinique", "973 - Guyane", "974 - La Réunion", "976 - Mayotte"];
	let departmentNames = ["Ain", "Aisne", "Allier", "Alpes-de-Haute-Provence", "Hautes-Alpes", "Alpes-Maritimes", "Ardèche", "Ardennes", "Ariège", "Aube", "Aude", "Aveyron", "Bouches-du-Rhône", "Calvados", "Cantal", "Charente", "Charente-Maritime", "Cher", "Corrèze", "Corse-du-Sud", "Haute-Corse", "Côte-d'Or", "Côtes-d'Armor", "Creuse", "Dordogne", "Doubs", "Drôme", "Eure", "Eure-et-Loir", "Finistère", "Gard", "Haute-Garonne", "Gers", "Gironde", "Hérault", "Ille-et-Vilaine", "Indre", "Indre-et-Loire", "Isère", "Jura", "Landes", "Loir-et-Cher", "Loire", "Haute-Loire", "Loire-Atlantique", "Loiret", "Lot", "Lot-et-Garonne", "Lozère", "Maine-et-Loire", "Manche", "Marne", "Haute-Marne", "Mayenne", "Meurthe-et-Moselle", "Meuse", "Morbihan", "Moselle", "Nièvre", "Nord", "Oise", "Orne", "Pas-de-Calais", "Puy-de-Dôme", "Pyrénées-Atlantiques", "Hautes-Pyrénées", "Pyrénées-Orientales", "Bas-Rhin", "Haut-Rhin", "Rhône", "Haute-Saône", "Saône-et-Loire", "Sarthe", "Savoie", "Haute-Savoie", "Paris", "Seine-Maritime", "Seine-et-Marne", "Yvelines", "Deux-Sèvres", "Somme", "Tarn", "Tarn-et-Garonne", "Var", "Vaucluse", "Vendée", "Vienne", "Haute-Vienne", "Vosges", "Yonne", "Territoire de Belfort", "Essonne", "Hauts-de-Seine", "Seine-Saint-Denis", "Val-de-Marne", "Val-d'Oise", "Guadeloupe", "Martinique", "Guyane", "La Réunion", "Mayotte"];

	useEffect(() => {
			fetch('/api/init_session', {
		}).then(res => res.json()).then(data => {
			if (!data) return;
			setClientKey(data);
		});
  	}, []);

	function resetSession() {
		setGameWon(false);
		setAttemptCount(0);
		setWhole([]);
		fetch('/api/reset_session', {
			headers: {
				'Content-Type': 'application/json'
			},
			method: 'POST',
			body: JSON.stringify({
				'client_key': clientKey,
			})
		}).then(res => res.json()).then(data => {
			if (!data) return;
			setClientKey(data);
		});
	}

	function handleSubmit(e) {
		e.preventDefault();
		if (!(departmentNames.includes(guess) || fullDepartmentNames.includes(guess))) {
			return;
		}
		fetch('/api/process_data', {
			headers: {
				'Content-Type': 'application/json'
			},
			method: 'POST',
			body: JSON.stringify({
				'client_key': clientKey,
				'found': gameWon['found'],
				'guess': guess.split(" - ")[0]
			})
		}).then(res => res.json()).then(data => {
			if (!data) return;
			let formatted = JSON.parse(data);
			setResult(formatted);
			setGameWon(formatted[Constants.FOUND]);
			setAttemptCount(formatted[Constants.ATTEMPTS]);
			whole.unshift(formatted);
			setWhole(whole);
		});
    }

	function handleChange(e) {
        setGuess(e.target.value);
        setResult("");
    }

	function WinMessage() {
		if (!gameWon)
			return;
		return (
			<div id="win_message">
            	<p>Félicitations vous avez trouvé en {attemptCount} essai(s) !</p>
				<a onClick={resetSession}>Rejouer</a>
        	</div>
		);
	}

	return (
	<>
		{!gameWon['found'] && <form onSubmit={handleSubmit}>
			<Autocomplete
				value={guess}
				onInput={handleChange}
				disablePortal
				options={fullDepartmentNames}
				sx={{ width: 300 }}
				onChange={(event, value) => setGuess(value)}
				renderInput={(params) => <TextField {...params} label={DEPARTMENTS_LABEL} />}
			/>
		</form>}
		<WinMessage/>
		<div id="game_div">
			<div id="categories">
				<span className="category">{DEPARTMENT_LABEL}</span>
				<span className="category">{PREFECTURE_LABEL}</span>
				<span className="category">{REGION_LABEL}</span>
				<span className="category">{TEL_AREA_CODE_LABEL}</span>
				<span className="category">{APEX_LABEL}</span>
				<span className="category">{SEAS_OCEANS_LABEL}</span>
				<span className="category">{PREFECTURE_POP_LABEL}</span>
				<span className="category">{DISTANCE_LABEL}</span>
				<span className="category">{NORTH_SOUTH_LABEL}</span>
				<span className="category">{EAST_WEST_LABEL}</span>
			</div>
			<div id="attempts">
				<Attempts props={whole}/>
			</div>
		</div>
	</>
	)
}

export default App
