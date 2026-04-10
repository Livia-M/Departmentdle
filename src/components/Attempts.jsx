/* Copyright (C) Livia Muamba - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Written by Livia Muamba, November 2025 */

import Attempt from './Attempt.jsx';
import Constants from '../constants/Constants.jsx';

export default function Attempts({props}) {
    return (
        <ul>
            {props.map(attempt => (
                <li key={attempt[Constants.ATTEMPTS]}>
                    <Attempt attempt={attempt}/>
                </li>
            ))}
        </ul>
    )
}