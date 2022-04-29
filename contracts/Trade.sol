// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.13;

import {ICurveV2} from "../interfaces/ICurveV2.sol";
import {IERC20} from "../interfaces/IERC20.sol";

contract Trader {
    ICurveV2 public POOL = ICurveV2(0x50f3752289e1456BfA505afd37B241bca23e685d);
    IERC20 public BADGER = IERC20(0x3472A5A71965499acd81997a54BBA8D852C6E53d);
    IERC20 public WBTC = IERC20(0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599);

    constructor() { 
        BADGER.approve(address(POOL), type(uint256).max);
        WBTC.approve(address(POOL), type(uint256).max);
    }

    function trade() external {
        POOL.exchange(0, 1, BADGER.balanceOf(address(this)), 0);
        POOL.exchange(1, 0, WBTC.balanceOf(address(this)), 0);
    }
}
