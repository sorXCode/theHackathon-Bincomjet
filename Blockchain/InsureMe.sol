pragma solidity >=0.4.25 <0.6.0;

contract InsureMe
{
    enum StateType{
        Registered,
        ObtainedPolicy,
        PolicyActive,
        Claim,
        PolicyClosed
    }
    // enum 
    enum PolicyDurationType {
        _3Months,
        _9Months,
        _12Months,
        _18Months,
        _24Months
        }

    enum PolicyType {
        Vehicle,
        Life,
        Health
    }

    struct User{
        string first_name;
        string last_name;
        string other_name;
        string phone;
        string email;
        int BVN; //Bank Verification Number of user
        string username;
        string[1] sex; //sex of user
        uint date; //Date of account creation
    }

    struct Description{
        string name;
        string id;
    }

    address public InstanceInsurer;
    PolicyType public Policy;
    PolicyDurationType public PolicyDuration;
    int public Premium;


    StateType public State;
    User UserInfo;

    address public InstanceInsured;
    // string public First_name;
    // int public AmountPaid;

    constructor(User memory details) public
    {
        InstanceInsured = msg.sender;
        UserInfo = details;
        State = StateType.Registered;
    }

    function TakePolicy(PolicyType policy,
                        PolicyDurationType duration,
                        description) public returns (string)
    {
        require(!checkItem(description), "Description exist in record");
        Policy = policy;
        PolicyDuration = duration;
        Description = description;
        Premium = calculatePremium();
        

    }

    function checkItem(description) public returns (bool)
    {
        //handle logic of contract here
        if (require(description == InstanceInsured.description,
                    "property already insured")){
                        return False;
                    }
        else{
            return True;
        }
    }

    function calculatePremium() public returns (int){
        //logic of calculation here
        return Premium;
    }


    function payPremium(int amount) public returns (string memory status){

    }
}