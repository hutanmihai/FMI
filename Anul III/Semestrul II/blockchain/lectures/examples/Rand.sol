// SPDX-License-Identifier: MIT

pragma solidity ^0.8.17;

import "https://github.com/smartcontractkit/chainlink/blob/develop/contracts/src/v0.8/vrf/interfaces/VRFCoordinatorV2Interface.sol";
import "https://github.com/smartcontractkit/chainlink/blob/develop/contracts/src/v0.8/vrf/VRFConsumerBaseV2.sol";
import "@chainlink/contracts/src/v0.8/ConfirmedOwner.sol";

//VRFCoordinatorV2Interface request randomness and manage subscriptions.
//VRFConsumerBaseV2 Communications with the consumer contracts

//https://docs.chain.link/vrf/v2/getting-started
//https://www.quicknode.com/guides/ethereum-development/smart-contracts/how-to-use-chainlink-vrf-in-your-smart-contract
//https://docs.chain.link/vrf
//https://chain.link/education-hub/blockchain-vs-oracles

contract Rand is VRFConsumerBaseV2, ConfirmedOwner {

    VRFCoordinatorV2Interface COORDINATOR;

    uint64 subscriptionId;
    address immutable linkToken;

    //functions as an ID of the offchain VRF job that runs in response to requests.
    bytes32 immutable keyHash;
    //The limit for how much gas to use for the callback request to your contract's fulfillRandomWords function.
    uint32 callbackGasLimit = 150000;
    uint16 requestConfirmations = 3;
    uint32 numWords = 1;
    uint public randomWordsNum;


    constructor(
        uint64 _subscriptionId
    )
        VRFConsumerBaseV2(0x8103B0A8A00be2DDC778e6e7eaa21791Cd364625)
        ConfirmedOwner(msg.sender)
    {
        COORDINATOR = VRFCoordinatorV2Interface(
            0x8103B0A8A00be2DDC778e6e7eaa21791Cd364625
        );
        
        subscriptionId = _subscriptionId;

        keyHash = 0x474e34a077df58807dbe9c96d3c009b23b3c6d0cce433e59bbf5b34f823bc56c;  
    }

    //requestRandomWords

    event RequestSent(uint256 requestId, uint32 numWords);
    event RequestFulfilled(uint256 requestId, uint256[] randomWords);

    struct RequestStatus {
        bool fulfilled; 
        bool exists; 
        uint256[] randomWords;
    }

    mapping(uint256 => RequestStatus)
        public requests; 

    uint256[] public requestIds;
    uint256 public lastRequestId;



    function requestRandomWords() public onlyOwner returns (uint256 requestId) {
        requestId = COORDINATOR.requestRandomWords(
            keyHash,
            subscriptionId,
            requestConfirmations,
            callbackGasLimit,
            numWords
        );

        requests[requestId] = RequestStatus({
            randomWords: new uint256[](0),
            exists: true,
            fulfilled: false
        });
    
        requestIds.push(requestId);
        lastRequestId = requestId;
        
        emit RequestSent(requestId, numWords);
        return requestId; 
    }


    function fulfillRandomWords(
        uint256 _requestId,
        uint256[] memory _randomWords
    ) internal override {
        require(requests[_requestId].exists, "request not found");
        requests[_requestId].fulfilled = true;
        requests[_requestId].randomWords = _randomWords;
        randomWordsNum = _randomWords[0]; 
        emit RequestFulfilled(_requestId, _randomWords);
    }

    function getRequestStatus(
        uint256 _requestId
    ) external view returns (bool fulfilled, uint256[] memory randomWords) {
        require(requests[_requestId].exists, "request not found");
        RequestStatus memory request = requests[_requestId];
        return (request.fulfilled, request.randomWords);
    }

    function getRandom() public returns (uint256 ) {
        uint256 requestId = requestRandomWords();
        uint256 rand = randomWordsNum % 1000;
        return rand;
    }

}