/* Copyright (C) Livia Muamba - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Written by Livia Muamba, November 2025 */

import Constants from '../constants/Constants.jsx';

export default function Attempt({attempt}) {
	return (
		<>
			<span className="department_name" animation="0"><p>{attempt[Constants.DEPARTMENT][0]}</p></span>
			<span className="cell" bg={attempt[Constants.PREFECTURE][1]} animation="1"><p>{attempt[Constants.PREFECTURE][0]}</p></span>
			<span className="cell" bg={attempt[Constants.REGION][1]} animation="2"><p>{attempt[Constants.REGION][0]}</p></span>
			<span className="cell" bg={attempt[Constants.TEL_AREA_CODE][1]} animation="3"><p>{attempt[Constants.TEL_AREA_CODE][0]}</p></span>
			<span className="cell" bg={attempt[Constants.APEX][2]} animation="4"><p>{attempt[Constants.APEX][0]}<br/>{attempt[Constants.APEX][1]}</p></span>
			<span className="cell" bg={attempt[Constants.SEAS_OCEANS][1]} animation="5"><p>{attempt[Constants.SEAS_OCEANS][0]}</p></span>
			<span className="cell" bg={attempt[Constants.PREFECTURE_POP][2]} animation="6"><p>{attempt[Constants.PREFECTURE_POP][0]}<br/>{attempt[Constants.PREFECTURE_POP][1]}</p></span>
			<span className="cell" bg={attempt[Constants.DISTANCE][1]} animation="7"><p>{attempt[Constants.DISTANCE][0]}</p></span>
			<span className="north_south" animation="8"><p>{attempt[Constants.NORTH_SOUTH][0]}</p></span>
			<span className="east_west" animation="9"><p>{attempt[Constants.EAST_WEST][0]}</p></span>
		</>
	)
}