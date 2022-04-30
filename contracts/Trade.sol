// SPDX-License-Identifier: UNLICENSED
pragma solidity 0.8.13;

import {ICurveV2} from "../interfaces/ICurveV2.sol";
import {IERC20} from "../interfaces/IERC20.sol";

contract Trader {
    ICurveV2 public pool;
    IERC20 public token0;
    IERC20 public token1;

    constructor(ICurveV2 _pool) { 
        pool = _pool;

        token0 = IERC20(_pool.coins(0));
        token1 = IERC20(_pool.coins(1));

        token0.approve(address(_pool), type(uint256).max);
        token1.approve(address(_pool), type(uint256).max);
    }

    function trade() external {
        pool.exchange(0, 1, token0.balanceOf(address(this)), 0);
        pool.exchange(1, 0, token1.balanceOf(address(this)), 0);
    }
}
