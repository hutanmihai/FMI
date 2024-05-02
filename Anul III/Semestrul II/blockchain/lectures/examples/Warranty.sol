// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.7.0 <0.9.0;

contract Warranty{

    enum Action { Replace, Repair, Refund, Reject, Sent } 

    struct Certificate{
        uint expirationDate;
        string terms;
        address provider;
    }

    struct Claim{
        address owner;
        uint productId;
        string request;
        Action action;
    }

    mapping (uint => Certificate) public certificates;
    mapping (uint => address) owners;

    Claim[] public claims;

    constructor() {

    }

    function purchase(uint productId) public {
        owners[productId] = msg.sender;
    }

    function provideCertificate(uint productId, uint expire, string memory terms) public{
    /*  certificates[productId].expirationDate = block.timestamp + expire;        
        certificates[productId].terms  = terms;
        certificates[productId].provider = msg.sender;
        */
        Certificate storage certificate = certificates[productId];
        certificate.expirationDate = block.timestamp + expire;        
        certificate.terms  = terms;
        certificate.provider = msg.sender;
    }

    function claim(uint productId, string memory request) public{
        claims.push(Claim({
            owner: msg.sender, 
            productId: productId, 
            request: request,
            action: Action.Sent}
            )
        );
    }

    function checkExpiration() public returns (uint expired) {
        expired = 0;
        for (uint p = 0; p < claims.length; p++) {
            if (certificates[claims[p].productId].expirationDate > block.timestamp) {
                expired+=1;
                claims[p].action = Action.Reject;
            }
        }
    }

    function repair(uint claimId) public returns (bool){
	require(certificates[claims[claimId].productId].expirationDate > block.timestamp, "Expired"); 
	require(certificates[claims[claimId].productId].provider == msg.sender, "Not the provider");     
        //if (certificates[claims[claimId].productId].expirationDate > block.timestamp
        //&& certificates[claims[claimId].productId].provider == msg.sender )
        claims[claimId].action = Action.Repair;
        return true;
    }


}