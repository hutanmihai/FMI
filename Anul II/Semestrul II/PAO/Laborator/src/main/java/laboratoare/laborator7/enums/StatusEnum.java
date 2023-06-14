package main.java.laboratoare.laborator7.enums;

/**
 * @author cvoinea
 */
public enum StatusEnum {
    PROCESSING ("processing") {
        @Override
        public int estimateDeliveryTime() {
            return 1;
        }
    },
    COMPLETE ("complete") {
        @Override
        public int estimateDeliveryTime() {
            return 0;
        }
    },
    RECEIVED ("received"){
        @Override
        public int estimateDeliveryTime() {
            return 2;
        }
    };

    private String name;

    StatusEnum(String name) {
        this.name = name;
    }



    public abstract int estimateDeliveryTime();

    public static StatusEnum fromValue(String input) {
        for (StatusEnum status : StatusEnum.values()) {
            if (status.name.equalsIgnoreCase(input.trim())) {
                return status;
            }
        }
        return null;
    }

}
